total_books_per_author <- dbGetQuery(con,
                                     
"SELECT a.author_id, firstname, lastname,  COUNT(*) AS total_books
 
FROM book b join author a on b.author_id = a.author_id
 
GROUP BY a.author_id")

top_author <- dbGetQuery(con, 
"SELECT a.firstname, COUNT(*) AS borrowed_count

FROM rental r

JOIN book b ON r.book_id = b.book_id

JOIN author a ON b.author_id = a.author_id

GROUP BY a.firstname

ORDER BY borrowed_count DESC

LIMIT 1")