var HortaApp = Ember.Application.create({
    LOG_TRANSITIONS : true,
});

HortaApp.store = DS.Store.create({
    revision : 11,
    adapter : DS.DjangoTastypieAdapter.extend(),
});

/* Models */
HortaApp.User = DS.Model.extend({
    name : DS.attr('string'),
});
HortaApp.Species = DS.Model.extend({
    name : DS.attr('string'),
    active : DS.attr('boolean'),
    created : DS.attr('date'),
    modified : DS.attr('date'),
    scientific_name : DS.attr('string'),
    description : DS.attr('string'),
    plantations : DS.hasMany('HortaApp.Plantation'),
});
HortaApp.Garden = DS.Model.extend({
    name : DS.attr('string'),
    active : DS.attr('boolean'),
    created : DS.attr('date'),
    modified : DS.attr('date'),
    geom : DS.attr('string'),
    parcels : DS.hasMany('HortaApp.Parcel'),

    wktParser : new OpenLayers.Format.WKT(),
    point : function(){
        var wkt = this.get('geom');
        var pt;
        if(wkt !== null){
            pt = this.wktParser.read(wkt);
        };
        return pt
    }.property('geom'),
});
HortaApp.Parcel = DS.Model.extend({
    name : DS.attr('string'),
    geom : DS.attr('string'),
    garden : DS.belongsTo('HortaApp.Garden'),
    zones : DS.hasMany('HortaApp.Zone'),
});
HortaApp.Zone = DS.Model.extend({
    name : DS.attr('string'),
    geom : DS.attr('string'),
    parcel : DS.belongsTo('HortaApp.Parcel'),
    plantations : DS.hasMany('HortaApp.Plantation'),
});
HortaApp.Plantation = DS.Model.extend({
    active : DS.attr('boolean'),
    created : DS.attr('date'),
    modified : DS.attr('date'),
    species : DS.hasMany('HortaApp.Species'),
    zone : DS.belongsTo('HortaApp.Zone'),
});

/* Views */
HortaApp.ApplicationView = Ember.View.extend({
    templateName : 'application',
});
HortaApp.AllGardensView = Ember.View.extend({
    templateName : 'all-gardens',
});
HortaApp.GardenView = Ember.View.extend({
    templateName : 'garden',
});
HortaApp.AllPlantationsView = Ember.View.extend({
    templateName : 'garden-plantations',
});
HortaApp.PlantationView = Ember.View.extend({
    templateName : 'plantation',
});
HortaApp.AllSpeciesView = Ember.View.extend({
    templateName : 'all-species',
});
HortaApp.SpeciesView = Ember.View.extend({
    templateName : 'species',
});

/* Controllers */
HortaApp.ApplicationController = Ember.Controller.extend();
HortaApp.AllGardensController = Ember.ArrayController.extend({
    totalGardens : function(){
        return this.get('length');
    }.property('@each'),
});
HortaApp.GardenController = Ember.ObjectController.extend({
});
HortaApp.AllPlantationsController = Ember.ArrayController.extend({
    needs : 'garden',
});
HortaApp.PlantationController = Ember.ObjectController.extend({
    teste : 'ardo',
});
HortaApp.AllSpeciesController = Ember.ArrayController.extend({
    totalSpecies : function(){
        return this.get('length');
    }.property('@each'),
});

/* Routers */
HortaApp.Router = Ember.Router.extend();
HortaApp.Router.map(function(){
    this.resource('allGardens', {path : '/garden'}, function(){
        this.resource('garden', {path : ':garden_id'}, function(){
            this.resource('allPlantations', {path : '/plantation'}, function(){
                this.resource('plantation', {path : ':plantation_id'});
            });
        });
    });
    this.resource('allSpecies', {path : '/species'});
    this.resource('species', {path : '/species/:species_id'});
});

HortaApp.AllGardensRoute = Ember.Route.extend({
    model : function(){
        return HortaApp.Garden.find();
    },
    setupController : function(controller, model){
        controller.set('content', model);
    },
});
HortaApp.GardenIndexRoute = Ember.Route.extend({
    model : function(params){
        return HortaApp.Garden.find(params.garden_id);
    },
    setupController : function(controller, model){
        controller.set('content', model);
    },
});
HortaApp.AllPlantationsRoute = Ember.Route.extend({
    model : function(){
        var the_garden = this.modelFor('garden');
        console.log('the_garden: '+ the_garden);
        return HortaApp.Plantation.find({zone__parcel__garden__id : the_garden.id});
    },
    setupController : function(controller, model){
        controller.set('content', model);
    },
});
HortaApp.PlantationRoute = Ember.Route.extend({
    model : function(params){
        //var the_plantation = this.modelFor('plantation');
        var fetched = HortaApp.Plantation.find(params.id);
        return fetched;
    },
    setupController : function(controller, model){
        controller.set('content', model);
    },
});
HortaApp.AllSpeciesRoute = Ember.Route.extend({
    model : function(){
        return HortaApp.Species.find();
    },
    setupController : function(controller, model){
        controller.set('content', model);
    },
});
HortaApp.SpeciesRoute = Ember.Route.extend({
    model : function(params){
        return HortaApp.Species.find(params.species_id);
    },
    setupController : function(controller, model){
        controller.set('content', model);
    },
});

HortaApp.initialize();
