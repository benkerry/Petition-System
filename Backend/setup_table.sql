CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT,
    stdid INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    hashed_pwd VARCHAR(255) NOT NULL,
    nickname VARCHAR(255) NOT NULL,
    root BOOLEAN NOT NULL,
    PRIMARY KEY(id),
    UNIQUE KEY nickname(nickname),
    UNIQUE KEY email(email)
);

CREATE TABLE petitions(
    id INT NOT NULL AUTO_INCREMENT,
    author_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    contents TEXT NOT NULL,
    supporters INT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    status INT NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT petitions_author_id_fkey FOREIGN KEY (author_id) REFERENCES users(id)
);

CREATE TABLE debates(
    id INT NOT NULL AUTO_INCREMENT,
    petition_id INT NOT NULL,
    author_id INT NOT NULL,
    contents TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY(id),
    CONSTRAINT debates_petition_id_fkey FOREIGN KEY (petition_id) REFERENCES petitions(id),
    CONSTRAINT debates_author_id_fkey FOREIGN KEY (author_id) REFERENCES users(id)
);

CREATE TABLE authcodes(
    stdid INT NOT NULL,
    code VARCHAR(255) NOT NULL,
    UNIQUE KEY stdid(stdid)
);