# Итоговое задание
```/api/medication```  
GET-запрос выведет список всех лекарств. POST-запрос создаст новое лекарство.  
Пример POST-запроса:
```
{
    "medication": {
        "m_name": "Спутник-V",
        "m_manufacuter_city": "Москва",
        "m_price": 1000,
        "m_pharmacy_id": 4
    }
}
```
```/api/medication?id=2```  
GET-запрос будет выводить информацию о лекарстве с определенным номером. PUT-запрос будет обновлять информацию об этом лекарстве.  
В PUT-запросе можно указывать лишь те параметры, которые нужно изменить.  
Пример PUT-запроса:
```
{
    "medication": {
        "m_name": "Пантенол",
        "m_price": 400
    }
}
```
```/api/medication?ph=3```  
Вывод списка лекарств, принадлежащих определенной аптеке. Параметр ph является номером аптеки.  
```/api/pharmacy```  
Список аптек.  
```/api/pharmacy?city=Ульяновск```  
Фильтрация аптек по городу.
