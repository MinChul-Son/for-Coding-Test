-- https://programmers.co.kr/learn/courses/30/lessons/59042?language=mysql
SELECT b.ANIMAL_ID, b.NAME FROM ANIMAL_INS a RIGHT OUTER JOIN ANIMAL_OUTS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE a.ANIMAL_ID IS NULL;


-- https://programmers.co.kr/learn/courses/30/lessons/59043?language=mysql
SELECT a.ANIMAL_ID, a.NAME FROM ANIMAL_INS a INNER JOIN ANIMAL_OUTS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE a.DATETIME > b.DATETIME
ORDER BY a.DATETIME;


