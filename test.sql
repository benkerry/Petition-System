INSERT INTO users(email, hashed_pwd, nickname, grade, priv, validated, expire_at, withdrawed) VALUES('', '', '', 1, 1, 1, DATE_ADD(NOW(), INTERVAL 10 MINUTE), 1);
INSERT INTO users(email, hashed_pwd, nickname, grade, priv, validated, expire_at, withdrawed) VALUES('12312312', '', '31212312', 1, 1, 1, DATE_ADD(NOW(), INTERVAL 10 MINUTE), 0);

INSERT INTO authcodes(grade, code, priv, expire_at) VALUES(0, '', 3, DATE_ADD(NOW(), INTERVAL 10 MINUTE));
INSERT INTO authcodes(grade, code, priv, expire_at) VALUES(0, '7797', 3, DATE_ADD(NOW(), INTERVAL 20 MINUTE));

INSERT INTO petitions(author_id, title, contents, created_at, expire_at, supports, reports, status, passed_at) VALUES(0, '', '', NOW(), DATE_ADD(NOW(), INTERVAL -1 DAY), 0, 0, 0, NOW());
INSERT INTO petitions(author_id, title, contents, created_at, expire_at, supports, reports, status, passed_at) VALUES(0, '', '', NOW(), DATE_ADD(NOW(), INTERVAL -1 DAY), 0, 0, 1, NOW());
INSERT INTO petitions(author_id, title, contents, created_at, expire_at, supports, reports, status, passed_at) VALUES(0, '', '', NOW(), DATE_ADD(NOW(), INTERVAL -1 DAY), 0, 0, 2, NOW());
INSERT INTO petitions(author_id, title, contents, created_at, expire_at, supports, reports, status, passed_at) VALUES(0, '', '', NOW(), DATE_ADD(NOW(), INTERVAL -1 DAY), 0, 0, 3, NOW());

INSERT INTO petitions(author_id, title, contents, created_at, expire_at, supports, reports, status, passed_at) VALUES(0, '', '', NOW(), DATE_ADD(NOW(), INTERVAL -1 DAY), 1, 0, 0, NOW());
INSERT INTO petitions(author_id, title, contents, created_at, expire_at, supports, reports, status, passed_at) VALUES(0, '', '', NOW(), DATE_ADD(NOW(), INTERVAL -1 DAY), 1, 0, 1, NOW());
INSERT INTO petitions(author_id, title, contents, created_at, expire_at, supports, reports, status, passed_at) VALUES(0, '', '', NOW(), DATE_ADD(NOW(), INTERVAL -1 DAY), 1, 0, 2, NOW());
INSERT INTO petitions(author_id, title, contents, created_at, expire_at, supports, reports, status, passed_at) VALUES(0, '', '', NOW(), DATE_ADD(NOW(), INTERVAL -1 DAY), 1, 0, 3, NOW());