var HortaApp = Ember.Application.create();

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
});

HortaApp.Garden = DS.Model.extend({
    name : DS.attr('string'),
    active : DS.attr('boolean'),
    created : DS.attr('date'),
    modified : DS.attr('date'),
    geom : DS.attr('string'),
    parcels : DS.hasMany('HortaApp.Parcel'),
});

HortaApp.Parcel = DS.Model.extend({
    name : DS.attr('string'),
    garden : DS.belongsTo('HortaApp.Garden'),
});

/* Views */
HortaApp.ApplicationView = Ember.View.extend({
    templateName : 'application',
});

HortaApp.AllGardensView = Ember.View.extend({
    templateName : 'all-gardens',
});
HortaApp.AllSpeciesView = Ember.View.extend({
    templateName : 'all-species',
});
HortaApp.GardenView = Ember.View.extend({
    templateName : 'garden',
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
HortaApp.AllSpeciesController = Ember.ArrayController.extend({
    totalSpecies : function(){
        return this.get('length');
    }.property('@each'),
});
HortaApp.GardenController = Ember.ObjectController.extend({
    wktParser : new OpenLayers.Format.WKT(),
    point : function(){
        var wkt = this.get('geom');
        var pt;
        if(wkt !== null){
            pt = this.wktParser.read(wkt);
        };
        return pt
    }.property('@each'),
});

/* Routers */
HortaApp.Router = Ember.Router.extend();
HortaApp.Router.map(function(){
    this.resource('allGardens', {path : '/garden'});
    this.resource('garden', {path : '/garden/:garden_id'});
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
HortaApp.AllSpeciesRoute = Ember.Route.extend({
    model : function(){
        return HortaApp.Species.find();
    },
    setupController : function(controller, model){
        controller.set('content', model);
    },
});
HortaApp.GardenRoute = Ember.Route.extend({
    model : function(params){
        return HortaApp.Garden.find(params.garden_id);
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
