create table userWishContext (
    wish_uid uuid,
    name char(256),
    start_ts date,
    end_ts date,
    price decimal(10,2),
    context char(1000),
    auto_renewable bool default false
);