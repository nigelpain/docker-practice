CREATE TABLE IF NOT EXISTS exercise_two (
    id bigint NOT NULL,
    first_name varchar(250) NOT NULL,
    CONSTRAINT exercise_two_pkey PRIMARY KEY (id)
);

INSERT INTO exercise_two(id, first_name) VALUES(1, 'Nigel');