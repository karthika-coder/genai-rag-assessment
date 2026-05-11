### Query: How does the system handle peak load?

**Strategy A (Raw Vector Search):**
- System scales horizontally using load balancers.
- Peak traffic managed with auto-scaling groups.
- Distributed queues handle high demand efficiently.

**Strategy B (Query Expansion):**
- System scales horizontally using load balancers.
- Distributed queues handle high demand efficiently.
- Peak traffic managed with auto-scaling groups.


### Query: What happens during traffic spikes?

**Strategy A (Raw Vector Search):**
- Peak traffic managed with auto-scaling groups.
- Caching reduces DB stress during spikes.
- Distributed queues handle high demand efficiently.

**Strategy B (Query Expansion):**
- Peak traffic managed with auto-scaling groups.
- Distributed queues handle high demand efficiently.
- Caching reduces DB stress during spikes.


### Query: Explain scaling under high demand.

**Strategy A (Raw Vector Search):**
- Distributed queues handle high demand efficiently.
- System scales horizontally using load balancers.
- Peak traffic managed with auto-scaling groups.

**Strategy B (Query Expansion):**
- System scales horizontally using load balancers.
- Distributed queues handle high demand efficiently.
- Peak traffic managed with auto-scaling groups.


