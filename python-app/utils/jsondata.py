import json

# Helper function for mocked data
def part_offers():
    data = '''
{
  "data": [
    {
      "part": {
        "id": "38945990",
        "partName": "ACS770ECB-200U-PFF-T",
        "sellers": [
          {
            "company": {
              "name": "DigiKey",
              "id": "459",
              "isVerified": true
            },
            "inventoryLevel": 5,
            "offers": [
              {
                "quantity": 1,
                "price": 10
              },
              {
                "quantity": 10,
                "price": 7.999
              },
              {
                "quantity": 100,
                "price": 7.39912
              }
            ]
          },
          {
            "company": {
              "name": "Mouser",
              "id": "2401",
              "isVerified": false
            },
            "inventoryLevel": 1000,
            "offers": [
              {
                "quantity": 1,
                "price": 10
              },
              {
                "quantity": 10,
                "price": 6.76
              },
              {
                "quantity": 50,
                "price": 6.76
              },
              {
                "quantity": 1000,
                "price": 5.74
              },
              {
                "quantity": 10000,
                "price": 5.59
              }
            ]
          },
          {
            "company": {
              "name": "Win Source",
              "id": "8706",
              "isVerified": true
            },
            "inventoryLevel": 0,
            "offers": []
          },
          {
            "company": {
              "name": "Arrow Electronics",
              "id": "1106",
              "isVerified": true
            },
            "inventoryLevel": 583,
            "offers": [
              {
                "quantity": 1,
                "price": 9.854
              },
              {
                "quantity": 10,
                "price": 6.715
              },
              {
                "quantity": 100,
                "price": 6.647
              },
              {
                "quantity": 1000,
                "price": 6.581
              },
              {
                "quantity": 10000,
                "price": 6.272
              }
            ]
          }
        ]
      }
    },
    {
      "part": {
        "id": "14377977",
        "partName": "RMD-53-66",
        "sellers": [
          {
            "company": {
              "name": "DigiKey",
              "id": "459",
              "isVerified": true
            },
            "inventoryLevel": 300,
            "offers": [
              {
                "quantity": 1,
                "price": 3
              },
              {
                "quantity": 10,
                "price": 2.55
              }
            ]
          },
          {
            "company": {
              "name": "TE Connectivity",
              "id": "8",
              "isVerified": true
            },
            "inventoryLevel": 3855,
            "offers": [
              {
                "quantity": 1,
                "price": 2.9
              },
              {
                "quantity": 10,
                "price": 2.9
              },
              {
                "quantity": 100,
                "price": 2.88
              },
              {
                "quantity": 1000,
                "price": 2.87
              },
              {
                "quantity": 10000,
                "price": 2.5
              }
            ]
          },
          {
            "company": {
              "name": "Arrow Electronics",
              "id": "1106",
              "isVerified": true
            },
            "inventoryLevel": 27005,
            "offers": [
              {
                "quantity": 1,
                "price": 3.3
              },
              {
                "quantity": 10000,
                "price": 1.2
              }
            ]
          }
        ]
      }
    },
    {
      "part": {
        "id": "82828282",
        "partName": "RN42XVP-IRM",
        "sellers": [
          {
            "company": {
              "name": "DigiKey",
              "id": "459",
              "isVerified": true
            },
            "inventoryLevel": 0,
            "offers": []
          },
          {
            "company": {
              "name": "Astin Ltd.",
              "id": "82881",
              "isVerified": false
            },
            "inventoryLevel": 24056,
            "offers": [
              {
                "quantity": 1,
                "price": 4.8
              },
              {
                "quantity": 10000,
                "price": 1.55
              }
            ]
          }
        ]
      }
    }
  ]
}
    '''
    return data