from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/products", 
                   responses={404: {"message": "No encontrado"}},
                   tags=["products"])

products_list = [
    {"id":1, "name": "Laptop", "price": 1000},  
    {"id":2, "name": "Smartphone", "price": 500}
]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}", status_code=200)
async def product_by_id(id: int):
    for product in products_list:
        if product["id"] == id:
            return product
    raise HTTPException(status_code=404, detail="Producto no encontrado")