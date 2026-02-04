import React from "react";

export default function EventCard({ event }) {
  return (
    <div style={{ border: "1px solid gray", padding: 10, margin: 5 }}>
      <p>Type: {event.type}</p>
      <pre>{JSON.stringify(event.payload, null, 2)}</pre>
    </div>
  );
}
