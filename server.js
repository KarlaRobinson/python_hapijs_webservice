'use strict';

const Hapi = require('hapi');

const server = new Hapi.Server();
server.connection({ port: 3000, host: 'localhost' });

server.register(require('inert'), (err) => {

    if (err) {
        throw err;
    }

    server.route({
        method: 'GET',
        path: '/',
        handler: function (request, reply) {
            reply.file('./book/index.html');
        }
    });

});

server.register(require('inert'), (err) => {

    if (err) {
        throw err;
    }

    server.route({
        method: 'GET',
        path: '/books',
        handler: function (request, reply) {
            reply.file('./book/index.html');
        }
    });

});

server.register(require('inert'), (err) => {

    if (err) {
        throw err;
    }

    server.route({
        method: 'POST',
        path: '/books/{id}',
        handler: function (request, reply) {
            reply('Searching');
            // var status = function () {this.reply('ok');};
        }
    });

});

server.register(require('inert'), (err) => {

    if (err) {
        throw {error: '', ok: false}
        // throw err;
    }

    server.route({
        method: 'GET',
        path: '/books/{id}',
        handler: function (request, reply) {
            reply.file('./book/show.html');
            // {
            // item: {title: '', author: '', id: ''},
            // ok: true
            // }
        }
    });

});

server.register(require('inert'), (err) => {

    if (err) {
        throw err;
    }

    server.route({
        method: 'POST',
        path: '/books',
        handler: function (request, reply) {
            reply.file('./book/index.html');
        }
    });

});

server.start((err) => {

    if (err) {
        throw err;
    }
    console.log(`Server running at: ${server.info.uri}`);
});