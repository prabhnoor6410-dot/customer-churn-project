import React from "react";
import {

  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,

  PieChart,
  Pie,
  Cell

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


const churnData = [

  {
    name: "Retained",
    value: 73.4
  },

  {
    name: "Churned",
    value: 26.6
  }

];


export default function Analytics() {

  return (

    <>

      <header className="page-header">

        <div>

          <p className="eyebrow">
            DATA ANALYTICS
          </p>

          <h2>
            Churn Analytics
          </h2>

          <p className="muted">
            Explore historical patterns
            from the Telco dataset.
          </p>

        </div>

      </header>


      <section className="analytics-grid">


        {/* CONTRACT CHART */}

        <div className="card chart-card">

          <h3>
            Churn by Contract
          </h3>

          <p className="chart-description">
            Historical churn percentage
            by contract type.
          </p>


          <ResponsiveContainer
            width="100%"
            height={340}
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
                formatter={value => [
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


        {/* PIE CHART */}

        <div className="card chart-card">

          <h3>
            Overall Churn Split
          </h3>

          <p className="chart-description">
            Dataset-level distribution.
          </p>


          <ResponsiveContainer
            width="100%"
            height={340}
          >

            <PieChart>

              <Pie
                data={churnData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                outerRadius={110}
                label
              >

                {churnData.map(
                  (_, index) => (

                    <Cell
                      key={index}
                    />

                  )
                )}

              </Pie>

              <Tooltip
                formatter={value =>
                  `${value}%`
                }
              />

            </PieChart>

          </ResponsiveContainer>

        </div>

      </section>


      <div className="card methodology">

        <h3>
          Analytics Methodology
        </h3>

        <p>

          The dashboard visualizes
          descriptive statistics and
          historical churn patterns.
          These charts describe
          associations in the dataset
          and do not by themselves
          establish causal relationships.

        </p>

      </div>

    </>

  );

}