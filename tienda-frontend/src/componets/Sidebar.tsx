"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Package, ShoppingCart, Home } from "lucide-react";

export default function Sidebar() {
  const pathname = usePathname();

  // Siempre mostrar el link de Home
  const links = [
    { href: "/", label: "Home", icon: <Home size={18} /> },
    { href: "/admin", label: "Productos", icon: <Package size={18} /> },
    { href: "/admin/sales", label: "Ventas", icon: <ShoppingCart size={18} /> },
  ];

  // Determinar si estamos en una ruta de admin
  const isAdminRoute = pathname.startsWith("/admin");

  // Filtrar los links según la ruta
  const visibleLinks = isAdminRoute
    ? links // mostrar todos los links si estamos en /admin
    : links.filter((link) => link.href === "/"); // solo Home si no

  return (
    <aside className="w-64 bg-gray-800 p-6 flex flex-col border-r border-gray-700">
      <h2 className="text-xl font-semibold mb-6 text-white">Panel Admin</h2>
      <nav className="flex flex-col gap-3">
        {visibleLinks.map((link) => {
          const isActive = pathname === link.href;
          return (
            <Link
              key={link.href}
              href={link.href}
              className={`flex items-center gap-2 px-3 py-2 rounded-lg transition ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-gray-300 hover:bg-gray-700 hover:text-white"
              }`}
            >
              {link.icon}
              <span>{link.label}</span>
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}
