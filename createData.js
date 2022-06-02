conn = new Mongo('127.0.0.1:27017')

db = conn.getDB("whales")

db.locations.insertMany([
    {
        _id: 1,
        breed: 'gray whale',
        pod: 'a',
        date: new Date("2021-11-12"),
        x: -122.3062,
        y: -47.6449
    },
    {
        _id: 2,
        breed: 'orca',
        pod: 'b',
        date: new Date("2022-05-04"),
        x: -124.4254,
        y: 47.2312
    },
    {
        _id: 3,
        breed: 'orca',
        pod: 'a',
        date: new Date("2022-07-06"),
        x: -126.3873,
        y: 73.2374
    },
    {
        _id: 4,
        breed: 'narwhal',
        pod: 'c',
        date: new Date("2021-12-07"),
        x: 25.8348,
        y: 100.2384
    }
])