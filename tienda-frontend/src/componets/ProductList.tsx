"use client";
import { useEffect, useState } from "react";
import { getProducts, createOrder } from "@/lib/api";

interface ProductResponse {
  id: number;
  product: {
    id: number;
    name: string;
    description: string;
    price: string;
  };
  quantity: number;
}

export default function ProductList({ admin = false }: { admin?: boolean }) {
  const [products, setProducts] = useState<ProductResponse[]>([]);
  const [phoneNumbers, setPhoneNumbers] = useState<{ [key: number]: string }>({});

  const loadProducts = async () => {
    try {
      const data = await getProducts();
      setProducts(data);
    } catch (err) {
      console.error(err);
      alert("❌ Error al cargar los productos");
    }
  };

  useEffect(() => {
    loadProducts();
  }, []);

  const handleInputChange = (id: number, value: string) => {
    setPhoneNumbers({ ...phoneNumbers, [id]: value });
  };

  const handleOrder = async (productId: number) => {
    const phone = phoneNumbers[productId];
    if (!phone || phone.trim().length < 6) {
      alert("Por favor ingresa un número de celular válido 📱");
      return;
    }

    try {
      await createOrder({ product_id: productId, quantity: 1, numero: phone });
      alert(`✅ Pedido creado correctamente para el número ${phone}`);
      setPhoneNumbers({ ...phoneNumbers, [productId]: "" });
    } catch (err) {
      console.error(err);
      alert("Error al crear el pedido");
    }
  };

  if (products.length === 0)
    return <p className="text-center mt-8 text-gray-400">No hay productos disponibles.</p>;

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
      {products.map((item) => (
        <div
          key={item.id}
          className="p-5 border border-gray-700 rounded-xl shadow-sm bg-gray-800 flex flex-col justify-between hover:bg-gray-750 transition"
        >
          <div>
            <h3 className="font-bold text-lg text-white">{item.product.name}</h3>
            <p className="text-sm text-gray-400 mt-1">{item.product.description}</p>
            <p className="text-green-400 font-semibold mt-3">
              ${parseFloat(item.product.price).toFixed(2)}
            </p>
            <p className="text-sm text-gray-500 mt-1">Stock: {item.quantity}</p>
          </div>

          {!admin && (
            <div className="mt-4">
              <input
                type="tel"
                placeholder="Número de celular"
                value={phoneNumbers[item.product.id] || ""}
                onChange={(e) => handleInputChange(item.product.id, e.target.value)}
                className="bg-gray-900 border border-gray-700 text-gray-200 p-2 w-full rounded mb-3 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <button
                onClick={() => handleOrder(item.product.id)}
                className="bg-green-600 text-white px-4 py-2 w-full rounded hover:bg-green-500 transition"
              >
                Ordenar
              </button>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
