-- 모든 레코드 조회하기
SELECT * 
    FROM ANIMAL_INS
    ORDER BY ANIMAL_ID;

-- 역순 정렬하기
SELECT NAME, DATETIME 
    FROM ANIMAL_INS
    ORDER BY ANIMAL_ID DESC;

-- 아픈 동물 찾기
SELECT ANIMAL_ID, NAME 
    FROM ANIMAL_INS
    WHERE INTAKE_CONDITION = 'Sick';

-- 어린 동물 찾기
SELECT ANIMAL_ID, NAME 
    FROM ANIMAL_INS
    WHERE INTAKE_CONDITION != 'Aged';

-- 동물의 아이디와 이름
SELECT animal_id, name 
    from animal_ins
    order by animal_id;

-- 여러기준으로 정렬하기
SELECT
    animal_id,
    name,
    datetime from animal_ins
order by 
    name asc, 
    datetime desc;

-- 상위 n개 레코드
SELECT NAME
    FROM ANIMAL_INS
    ORDER BY DATETIME
    LIMIT 1;