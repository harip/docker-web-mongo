var cfg = { _id: 'webdemors',
    members: [
        { _id: 0, host: 'db1:27017'},
        { _id: 1, host: 'db2:27017'},
        { _id: 2, host: 'db3:27017'}
    ]
};
var error = rs.initiate(cfg);