/*
 *
 */

Ember.TEMPLATES['application'] = Ember.Handlebars.compile('' +
    '<h1>Gardens App - Initial versions</h1>' +
    '{{outlet}}'
);

Ember.TEMPLATES['gardenIndex'] = Ember.Handlebars.compile('' +
    '{{#each content}}' +
        '<h2>{{name}}</h2>' +
        '<div class="createdDate">{{formattedDate}}</div>' +
        '<hr class="separator" />' +
    '{{/each}}'
);
