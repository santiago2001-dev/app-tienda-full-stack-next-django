"use client";
import { useEffect, useState } from "react";

export default function SalesList() {
  const [sales, setSales] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const loadSales = async () => {
    try {
      const res = await fetch("http://localhost:8000/api/sales/");
      if (!res.ok) throw new Error("Error al cargar ventas");
      const data = await res.json();
      setSales(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadSales();
  }, []);

  if (loading) return <p className="text-center mt-10 text-gray-300">Cargando ventas...</p>;

  return (
    <div className="p-6 text-gray-100">
      <h1 className="text-2xl font-bold mb-4">Listado de Ventas</h1>

      {sales.length === 0 ? (
        <p className="text-gray-400">No hay ventas registradas.</p>
      ) : (
        <div className="overflow-x-auto bg-gray-800 rounded-lg shadow-md border border-gray-700">
          <table className="min-w-full text-left border-collapse">
            <thead className="bg-gray-700 text-gray-200">
              <tr>
                <th className="px-4 py-3 border-b border-gray-600">ID</th>
                <th className="px-4 py-3 border-b border-gray-600">Producto</th>
                <th className="px-4 py-3 border-b border-gray-600">Cantidad</th>
                <th className="px-4 py-3 border-b border-gray-600">Precio Total</th>
                <th className="px-4 py-3 border-b border-gray-600">Fecha</th>
              </tr>
            </thead>
            <tbody>
              {sales.map((s) => (
                <tr
                  key={s.id}
                  className="border-b border-gray-700 hover:bg-gray-700 transition"
                >
                  <td className="px-4 py-3">{s.id}</td>
                  <td className="px-4 py-3 font-medium text-gray-100">{s.product.name}</td>
                  <td className="px-4 py-3">{s.quantity}</td>
                  <td className="px-4 py-3 font-semibold text-green-400">
                    ${parseFloat(s.total_price).toFixed(2)}
                  </td>
                  <td className="px-4 py-3 text-gray-400">
                    {new Date(s.created_at).toLocaleString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
