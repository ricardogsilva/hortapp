var HortaApp = Ember.Application.create();

HortaApp.store = DS.Store.create({
    revision : 11,
    adapter : DS.DjangoTastypieAdapter.extend(),
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
HortaApp.ApplicationController = Ember.Controller.extend({
    teste : 'Ricardo',
    coisas : ['isto', 'aquilo', 'o outro', 'mais um'],
});
HortaApp.AllGardensController = Ember.ArrayController.extend();

/* Routers */
HortaApp.Router = Ember.Router.extend();
HortaApp.Router.map(function(){
    this.resource('allGardens', {path : '/garden'}, function(){
        this.route('new');
    });
});

HortaApp.AllGardensRoute = Ember.Route.extend({
    model : function(){
        var coisas = HortaApp.Garden.find();
        console.log(coisas);
        return coisas;
    },
    setupController : function(controller, model){
        console.log('aqui');
        controller.set('content', model);
        console.log('ali');
    },
});

HortaApp.initialize();
