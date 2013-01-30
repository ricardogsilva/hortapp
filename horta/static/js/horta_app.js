var HortaApp = Ember.Application.create();

HortaApp.store = DS.Store.create({
    revision : 11,
    adapter : DS.DjangoTastypieAdapter.extend(),
});

/* Models */
HortaApp.Garden = DS.Model.extend({
    name : DS.attr('string'),
    active : DS.attr('boolean'),
    created : DS.attr('date'),
    modified : DS.attr('date'),
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

/* Controllers */
HortaApp.ApplicationController = Ember.Controller.extend();
HortaApp.AllGardensController = Ember.ArrayController.extend({
    totalGardens : function(){
        console.log(this);
        return this.get('length');
    }.property('@each'),
});
HortaApp.GardenController = Ember.ObjectController.extend();

/* Routers */
HortaApp.Router = Ember.Router.extend();
HortaApp.Router.map(function(){
    this.resource('allGardens', {path : '/garden'});
    this.resource('garden', {path : '/garden/:garden_id'});
});

HortaApp.AllGardensRoute = Ember.Route.extend({
    model : function(){
        return HortaApp.Garden.find();
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

HortaApp.initialize();
