var HortaApp = Ember.Application.create({
    ready : function(){
        console.log('ric');
        //var gardens = HortaApp.Garden.find();
        //console.log(gardens);
        //console.log('rac');
    },
});

HortaApp.store = DS.Store.create({
    revision : 11,
    adapter : DS.DjangoTastypieAdapter.extend({
    }),
});

/* Models */
HortaApp.Garden = DS.Model.extend({
    name : DS.attr('string'),
    //active : DS.attr('boolean'),
    //created : DS.attr('date'),
    //modified : DS.attr('date'),
});

/* Views */
HortaApp.ApplicationView = Ember.View.extend({
    templateName : 'application',
});

HortaApp.AllGardensView = Ember.View.extend({
    templateName : 'all-gardens',
});

/* Controllers */
HortaApp.ApplicationController = Ember.Controller.extend();
HortaApp.AllGardensController = Ember.ArrayController.extend();

/* Routers */
HortaApp.Router = Ember.Router.extend();
HortaApp.Router.map(function(match){
    match('/').to('allGardens');
});

HortaApp.AllGardensRoute = Ember.Route.extend({
    setupControllers : function(controller){
        controller.set('gardens', HortaApp.Garden.find());
    },
});

HortaApp.initialize();
