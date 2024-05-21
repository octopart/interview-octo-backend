import json

# Helper function for mocked data
def part_offers():
    data = '''
    {
       "part":{
          "id":"38945990",
          "mpn":"ACS770ECB-200U-PFF-T",
          "sellers":[
             {
                "company":{
                   "name":"DigiKey",
                   "id":"459",
                   "isVerified":true
                },
                "offers":[
                   {
                      "inventoryLevel": 5,
                      "prices":[
                         {
                            "quantity":1,
                            "price":10
                         },
                         {
                            "quantity":10,
                            "price":7.999
                         },
                         {
                            "quantity":100,
                            "price":7.39912
                         }
                      ]
                   }
                ]
             },
             {
                "company":{
                   "name":"Mouser",
                   "id":"2401",
                   "isVerified":false
                },
                "offers":[
                   {
                      "inventoryLevel": 1000,
                      "prices":[
                         {
                            "quantity":1,
                            "price":10
                         },
                         {
                            "quantity":10,
                            "price":6.76
                         },
                         {
                            "quantity":50,
                            "price":6.76
                         },
                         {
                            "quantity":1000,
                            "price":5.74
                         },
                         {
                            "quantity":10000,
                            "price":5.59
                         }
                      ]
                   }
                ]
             },
             {
                "company":{
                   "name":"Win Source",
                   "id":"8706",
                   "isVerified":true
                },
                "offers":[
                   {
                      "inventoryLevel": 0,
                      "prices":[]
                   }
                ]
             },
             {
                "company":{
                   "name":"Arrow Electronics",
                   "id":"1106",
                   "isVerified":true
                },
                "offers":[
                   {
                      "inventoryLevel": 583,
                      "prices":[
                         {
                            "quantity":1,
                            "price":9.854
                         },
                         {
                            "quantity":10,
                            "price":6.715
                         },
                         {
                            "quantity":100,
                            "price":6.647
                         },
                         {
                            "quantity":1000,
                            "price":6.581
                         },
                         {
                            "quantity":10000,
                            "price":6.272
                         }
                      ]
                   }
                ]
             }
          ]
       }
    }
    '''
    print(data)
    return data