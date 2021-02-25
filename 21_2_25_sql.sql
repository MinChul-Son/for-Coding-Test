-- https://programmers.co.kr/learn/courses/30/lessons/59042?language=mysql
SELECT b.ANIMAL_ID, b.NAME FROM ANIMAL_INS a RIGHT OUTER JOIN ANIMAL_OUTS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE a.ANIMAL_ID IS NULL;


-- https://programmers.co.kr/learn/courses/30/lessons/59043?language=mysql
SELECT a.ANIMAL_ID, a.NAME FROM ANIMAL_INS a INNER JOIN ANIMAL_OUTS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE a.DATETIME > b.DATETIME
ORDER BY a.DATETIME;


-- https://programmers.co.kr/learn/courses/30/lessons/59044?language=mysql
SELECT a.NAME, a.DATETIME FROM ANIMAL_INS a LEFT OUTER JOIN ANIMAL_OUTS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE b.ANIMAL_ID IS NULL
ORDER BY a.DATETIME
LIMIT 3;


-- https://programmers.co.kr/learn/courses/30/lessons/59045?language=mysql
SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME FROM ANIMAL_INS a INNER JOIN ANIMAL_OUTS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE a.SEX_UPON_INTAKE <> b.SEX_UPON_OUTCOME;