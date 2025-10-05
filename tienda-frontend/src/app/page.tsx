import ProductList from "@/componets/ProductList";

export default function Home() {
  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold mb-4">🛍️ Tienda</h1>
      <ProductList />
    </main>
  );
}
