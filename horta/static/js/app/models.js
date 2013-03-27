/*
 *
 */

Horta.Garden = DS.Model.extend({
    name : DS.attr('string'),
    active : DS.attr('boolean'),
    created : DS.attr('date'),
    modified : DS.attr('date'),
    geom : DS.attr('string'),
    //parcels : DS.hasMany('HortaApp.Parcel'),

    formattedDate : function(){
        var d = this.get('created');
        var formattedDate = '';
        if(d){
             formattedDate = d.getUTCDate() + '/' + 
                (d.getUTCMonth() + 1) + '/' + d.getUTCFullYear();
        }
        return formattedDate;
    }.property('created').cacheable(),
});
