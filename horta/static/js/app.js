/*Application*/
var HortaApp = Ember.Application.create({
    /*additional properties can go here*/
    author : 'Ricardo',
    //ready : function(){
    //    alert('Ember a bombar!');
    //},
});

/*Models*/
HortaApp.Garden = Ember.Object.extend({
    name : null,
});
HortaApp.Garden.reopenClass({
    allGardens : [],
    find : function(){
        $.ajax({
            url : 'http://localhost:8000/api/v1/garden/',
            dataType : 'json',
            context : this,
            success : function(response){
                alert('ric');
                //response.data.forEach(function(garden){
                //    this.allGardens.addObject(HortaApp.Garden.create(garden))
                //}, this)
            }
        })
        return this.allGardens;
    },
});

/*
HortaApp.Contributor = Ember.Object.extend();
HortaApp.Contributor.reopenClass({
    allContributors : [],
    find : function(){
        $.ajax({
            url : 'https://api.github.com/repos/emberjs/ember.js/contributors',
            dataType: 'jsonp',
            context : this,
            success : function(response){
                response.data.forEach(function(contributor){
                    this.allContributors.addObject(
                        HortaApp.Contributor.create(contributor))
                }, this)
            }
        })
        return this.allContributors;
    },
    findOne : function(username){
        var contributor = HortaApp.Contributor.create({
            login : username,
        });
        $.ajax({
            url : 'https://api.github.com/repos/emberjs/ember.js/contributors',
            dataType : 'jsonp',
            context : contributor,
            success : function(response){
                this.setProperties(response.data.findProperty('login', username));
            }
        })
        return contributor;
    },
});
*/

/*Views*/
HortaApp.ApplicationView = Ember.View.extend({
    templateName : 'horta application',
});
/*
HortaApp.AllContributorsView = Ember.View.extend({
    templateName : 'contributors',
});
HortaApp.OneContributorView = Ember.View.extend({
    templateName : 'a-contributor',
});
HortaApp.DetailsView = Ember.View.extend({
    templateName : 'contributor-details',
});
*/
HortaApp.AllGardensView = Ember.View.extend({
    templateName : 'gardens',
});

/*Controllers*/
HortaApp.ApplicationController = Ember.Controller.extend();
/*
HortaApp.AllContributorsController = Ember.ArrayController.extend();
HortaApp.OneContributorController = Ember.ObjectController.extend();
*/
HortaApp.AllGardensController = Ember.ArrayController.extend();

/*Routers*/
HortaApp.Router = Ember.Router.extend({
    enableLogging : true,
    root : Ember.Route.extend({
        //contributors : Ember.Route.extend({
        //    route : '/',
        //    showContributor : Ember.Route.transitionTo('aContributor'),
        //    connectOutlets : function(router){
        //        router.get('applicationController').connectOutlet(
        //            'allContributors',
        //            HortaApp.Contributor.find());
        //    },
        //}),
        //aContributor : Ember.Route.extend({
        //    route : '/:githubUserName',
        //    showAllContributors : Ember.Route.transitionTo('contributors'),
        //    connectOutlets : function(router, context){
        //        router.get('applicationController').connectOutlet(
        //            'oneContributor', context);
        //    },
        //    serialize : function(router, context){
        //        return {
        //            githubUserName : context.get('login')
        //        }
        //    },
        //    deserialize : function(router, urlParams){
        //        return HortaApp.Contributor.findOne(urlParams.githubUserName);
        //    },

        //    //child states

        //    initialState : 'details',
        //    details : Ember.Route.extend({
        //        route: '/',
        //        connectOutlets: function(router){
        //            router.get('oneContributorController').connectOutlet('details');
        //        }
        //    }),
        //    repos : Ember.Route.extend({
        //        route : '/repos',
        //        connectOutlets : function(router){
        //            router.get('oneContributorController').connectOutlet('repos');
        //        }
        //    }),
        //}),
        gardens : Ember.Route.extend({
            route : '/',
            showGarden : Ember.Route.transitionTo('aGarden'),
            connectOutlets : function(router){
                router.get('applicationController').connectOutlet(
                    'allGardens',
                    HortaApp.Garden.find());
            },
        }),
    })
});

HortaApp.initialize();
