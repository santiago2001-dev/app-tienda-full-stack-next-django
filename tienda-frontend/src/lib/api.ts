const API_BASE = "http://localhost:8000/api"; // Reemplázalo con la base real de tu API

export const getProducts = async () => {
  const res = await fetch(`${API_BASE}/products/stock/`);
  if (!res.ok) throw new Error("Error al obtener productos");
  return res.json();
};

export const getSales =  async ()=>{
    const res = await fetch(`${API_BASE}/sales/`);
    if (!res.ok) throw new Error("Error al obtener productos");
    return res.json();
}
export const createProduct = async (product: {
  name: string;
  price: number;
  description: string;
  quantity : number;
}) => {
  const res = await fetch(`${API_BASE}/products/create_product/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(product),
  });
  if (!res.ok) throw new Error("Error al crear producto");
  return res.json();
};

export const createOrder = async (order: { product_id: number; quantity: number,numero :string }) => {
  const res = await fetch(`${API_BASE}/sales/create/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(order),
  });
  if (!res.ok) throw new Error("Error al crear pedido");
  return res.json();
};
