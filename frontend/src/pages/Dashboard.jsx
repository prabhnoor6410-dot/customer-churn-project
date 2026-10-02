import React from "react";
import {
  Users,
  UserRoundX,
  TrendingDown,
  DollarSign
} from "lucide-react";

import {
  Link
} from "react-router-dom";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";


const contractData = [

  {
    name: "Month-to-month",
    churn: 42.7
  },

  {
    name: "One year",
    churn: 11.3
  },

  {
    name: "Two year",
    churn: 2.8
  }

];


export default function Dashboard() {

  return (

    <>

      {/* HEADER */}

      <header className="page-header">

        <div>

          <p className="eyebrow">
            CUSTOMER CHURN INTELLIGENCE
          </p>

          <h2>
            Executive Dashboard
          </h2>

          <p className="muted">
            Monitor customer retention
            and identify churn risk.
          </p>

        </div>


        <Link
          className="primary-btn"
          to="/prediction"
        >
          Run Prediction
        </Link>

      </header>


      {/* KPI CARDS */}

      <section className="kpi-grid">

        <KPI
          icon={<Users />}
          title="Total Customers"
          value="7,032"
          note="Cleaned dataset"
        />

        <KPI
          icon={<UserRoundX />}
          title="Churned Customers"
          value="1,869"
          note="Historical churn"
        />

        <KPI
          icon={<TrendingDown />}
          title="Churn Rate"
          value="26.6%"
          note="Overall dataset rate"
        />

        <KPI
          icon={<DollarSign />}
          title="Avg. Monthly Charge"
          value="$64.76"
          note="Across customers"
        />

      </section>


      {/* CHART + INSIGHTS */}

      <section className="content-grid">


        <div className="card chart-card">

          <div className="card-heading">

            <div>

              <h3>
                Churn Rate by Contract
              </h3>

              <p>
                Historical churn percentage
              </p>

            </div>

          </div>


          <ResponsiveContainer
            width="100%"
            height={310}
          >

            <BarChart
              data={contractData}
            >

              <CartesianGrid
                strokeDasharray="3 3"
              />

              <XAxis
                dataKey="name"
              />

              <YAxis
                unit="%"
              />

              <Tooltip
                formatter={(value) => [
                  `${value}%`,
                  "Churn"
                ]}
              />

              <Bar
                dataKey="churn"
                radius={[
                  7,
                  7,
                  0,
                  0
                ]}
              />

            </BarChart>

          </ResponsiveContainer>

        </div>


        {/* INSIGHTS */}

        <div className="card insight-card">

          <h3>
            Project Insights
          </h3>


          <Insight
            number="01"
            title="Contract matters"
            text="Contract type is an important segmentation variable for churn analysis."
          />


          <Insight
            number="02"
            title="Tenure matters"
            text="Customer tenure can help identify early lifecycle retention risk."
          />


          <Insight
            number="03"
            title="Use the ML model"
            text="Enter customer attributes to receive an individual churn prediction."
          />

        </div>

      </section>

    </>

  );
}


/* KPI COMPONENT */

function KPI({
  icon,
  title,
  value,
  note
}) {

  return (

    <div className="card kpi">

      <div className="kpi-icon">
        {icon}
      </div>

      <div>

        <p>
          {title}
        </p>

        <h3>
          {value}
        </h3>

        <span>
          {note}
        </span>

      </div>

    </div>

  );

}


/* INSIGHT COMPONENT */

function Insight({
  number,
  title,
  text
}) {

  return (

    <div className="insight">

      <span className="insight-number">
        {number}
      </span>

      <div>

        <strong>
          {title}
        </strong>

        <p>
          {text}
        </p>

      </div>

    </div>

  );

}