SELECT a.id, a.title, a.text
FROM article a
WHERE NOT EXISTS (SELECT 1 FROM comment c WHERE c.article_id = a.id)