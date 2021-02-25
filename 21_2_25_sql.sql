-- https://programmers.co.kr/learn/courses/30/lessons/59042?language=mysql
SELECT b.ANIMAL_ID, b.NAME FROM ANIMAL_INS a RIGHT OUTER JOIN ANIMAL_OUTS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE a.ANIMAL_ID IS NULL;



