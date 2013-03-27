/*
 *
 */

var Horta = Ember.Application.create({
    LOG_TRANSITIONS : true,
});

Horta.store = DS.Store.create({
    revision : 11,
    adapter : DS.DjangoTastypieAdapter.extend(),
});
