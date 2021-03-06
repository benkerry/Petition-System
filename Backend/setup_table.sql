CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    hashed_pwd VARCHAR(255) NOT NULL,
    nickname VARCHAR(255) NOT NULL,
    grade INT NOT NULL,
    priv INT NOT NULL,
    validated BOOLEAN NOT NULL,
    expire_at DATETIME NOT NULL,
    withdrawed BOOLEAN NOT NULL DEFAULT 0,
    PRIMARY KEY(id),
    UNIQUE  KEY nickname(nickname),
    UNIQUE KEY email(email)
) DEFAULT CHARSET=UTF8;

CREATE TABLE petitions(
    id INT NOT NULL AUTO_INCREMENT,
    author_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    contents TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    expire_at DATETIME NOT NULL,
    supports INT NOT NULL DEFAULT 0,
    reports INT NOT NULL DEFAULT 0,
    status INT NOT NULL DEFAULT 0,
    passed_at DATETIME,
    PRIMARY KEY(id)
) DEFAULT CHARSET=UTF8;

CREATE TABLE notices(
    id INT NOT NULL AUTO_INCREMENT,
    author_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    contents TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY(id)
) DEFAULT CHARSET=UTF8;

CREATE TABLE supports(
    uid INT NOT NULL,
    petition_id INT NOT NULL
) DEFAULT CHARSET=UTF8;

CREATE TABLE authcodes(
    grade INT NOT NULL,
    code VARCHAR(255) NOT NULL,
    priv INT NOT NULL,
    expire_at DATETIME NOT NULL,
    UNIQUE KEY code(code)
) DEFAULT CHARSET=UTF8;

CREATE TABLE reports(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    uid INT NOT NULL,
    petition_id INT NOT NULL,
    description TEXT NOT NULL
) DEFAULT CHARSET=UTF8;