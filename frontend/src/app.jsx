import React from "react";

import {
  NavLink,
  Routes,
  Route,
} from "react-router-dom";

import {
  LayoutDashboard,
  Users,
  Brain,
  BarChart3,
} from "lucide-react";

import Dashboard from "./pages/Dashboard";
import Prediction from "./pages/Prediction";
import Analytics from "./pages/Analytics";
import Customers from "./pages/Customers";

export default function App() {
  return (
    <div className="app-shell">

      {/* SIDEBAR */}
      <aside className="sidebar">

        <div className="brand">

          <div className="brand-mark">
            C
          </div>

          <div>
            <h1>ChurnIQ</h1>

            <span>
              Customer Intelligence
            </span>
          </div>

        </div>

        {/* NAVIGATION */}
        <nav className="nav">

          <NavLink to="/" end>
            <LayoutDashboard size={19} />
            Dashboard
          </NavLink>

          <NavLink to="/prediction">
            <Brain size={19} />
            Prediction
          </NavLink>

          <NavLink to="/analytics">
            <BarChart3 size={19} />
            Analytics
          </NavLink>

          <NavLink to="/customers">
            <Users size={19} />
            Customers
          </NavLink>

        </nav>

        {/* SIDEBAR FOOTER */}
        <div className="sidebar-footer">

          <span className="status-dot"></span>

          ML API

        </div>

      </aside>

      {/* MAIN CONTENT */}
      <main className="main-content">

        <Routes>

          <Route
            path="/"
            element={<Dashboard />}
          />

          <Route
            path="/prediction"
            element={<Prediction />}
          />

          <Route
            path="/analytics"
            element={<Analytics />}
          />

          <Route
            path="/customers"
            element={<Customers />}
          />

        </Routes>

      </main>

    </div>
  );
}