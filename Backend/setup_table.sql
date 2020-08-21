CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    hashed_pwd VARCHAR(255) NOT NULL,
    nickname VARCHAR(255) NOT NULL,
    grade INT NOT NULL,
    root BOOLEAN NOT NULL,
    validated BOOLEAN NOT NULL,
    withdraw_at DATETIME,
    PRIMARY KEY(id),
    UNIQUE  KEY nickname(nickname),
    UNIQUE KEY email(email)
);

CREATE TABLE petitions(
    id INT NOT NULL AUTO_INCREMENT,
    author_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    contents TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    supports INT NOT NULL DEFAULT 0,
    status INT NOT NULL DEFAULT 0,
    passed_at DATETIME,
    PRIMARY KEY(id),
    CONSTRAINT petitions_author_id_fkey FOREIGN KEY (author_id) REFERENCES users(id)
);

CREATE TABLE supports(
    uid INT NOT NULL,
    petition_id INT NOT NULL,
    CONSTRAINT supports_uid_fkey FOREIGN KEY (uid) REFERENCES users(id),
    CONSTRAINT supports_petition_id_fkey FOREIGN KEY (petition_id) REFERENCES petitions(id)
);    ㅇ

CREATE TABLE authcodes(
    stdid INT NOT NULL,
    code VARCHAR(255) NOT NULL,
    root INT NOT NULL,
    UNIQUE KEY stdid(stdid),
    UNIQUE KEY code(code)
);