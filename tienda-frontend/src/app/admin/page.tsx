"use client";


import ProductForm from "@/componets/ProductForm";
import ProductList from "@/componets/ProductList";
import { useState } from "react";

export default function AdminPage() {
  const [reload, setReload] = useState(false);
  const refresh = () => setReload(!reload);

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Gestión de Productos</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-gray-800 p-6 rounded-2xl shadow">
          <h2 className="text-lg font-semibold mb-4 text-gray-200">Crear Producto</h2>
          <ProductForm onCreated={refresh} />
        </div>

        <div className="bg-gray-800 p-6 rounded-2xl shadow">
          <h2 className="text-lg font-semibold mb-4 text-gray-200">Listado de Productos</h2>
          <ProductList key={reload.toString()} admin />
        </div>
      </div>
    </div>
  );
}
