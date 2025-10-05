"use client";
import { useState } from "react";
import { createProduct } from "@/lib/api";

export default function ProductForm({ onCreated }: { onCreated: () => void }) {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [description, setDescription] = useState("");
  const [quantity, setQuantity] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name || !price || !description || !quantity) return alert("Completa todos los campos");

    await createProduct({ name,  price : parseInt(price), description, quantity: parseInt(quantity) });
    onCreated();
    setName("");
    setPrice("");
    setDescription("");
    setQuantity("");
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-200">Nombre</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-gray-100 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Nombre del producto"
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-200">Precio</label>
        <input
          type="number"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-gray-100 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Precio"
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-200">Descripción</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-gray-100 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Descripción del producto"
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-200">Cantidad disponible</label>
        <input
          type="number"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          className="w-full p-2 rounded bg-gray-700 border border-gray-600 text-gray-100 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Cantidad disponible"
        />
      </div>

      <button
        type="submit"
        className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded font-medium"
      >
        Guardar
      </button>
    </form>
  );
}
