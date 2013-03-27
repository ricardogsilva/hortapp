/*
 *
 */

Horta.Router = Ember.Router.extend({
    location : 'hash',
});

Horta.Router.map(function(){
    this.route('index', {path : '/'});
    this.route('gardenIndex', {path : '/garden'});
});

Horta.IndexRoute = Ember.Route.extend({
    redirect : function(){
        this.transitionTo('gardenIndex');
    },
});
Horta.GardenIndexRoute = Ember.Route.extend({
    model : function(){
        return Horta.Garden.find();
    },
});
