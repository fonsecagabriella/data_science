# C1M3 - Data Architecture

- Enterprise architecture is the design of systems to support change in an enterprise, achieved by flexible and reversible decisions reached through a careful evaluation of trade-offs.

- Conway's Law: Any organisation that designs a system will produce a design whose structure is a copy of the organisation's communication structure.

## Principles of good data architecture

- The principles can be "divided" into 3 groups:
    - How data impacts others in the organisation
    - Ongoing process, evolving over time
    - Unspoken but understood priorities

- **1. Choose common components wisely**
- **2. Architecture is leadership**
    - Facilitates team collaboration
    - Break down silos
    - Avoid a 'one size fits all' approach

- **3. Always be architecting**
- **4. Make reversible decisions**
- **5. Build loosely coupled systems**
    - System's built avoid reversible decisions allows you to be always architecting, always improving
    - Use API's to serve data

- **6. Plan for fail**
    - Take a practical and quantitative approach (availability or uptime, reliability, durability)
    - Recovery time objective (RTO): Maximum acceptable time for a service of system outage
    - Recovery point objective (RPO): Acceptable state after recovery (ie, maximum acceptable data loss)
- **7. Prioritise security**
    - Zero-trust security: every action required authentication
- **8. Architect for scalability**
- **9. Embrace FinOps**
    - Embrace FinOps to manage cloud cost: how is the most cost efficient way to run?

## Batch architectures

- Most practical when real-time analysis is not critical
- Data is ingested >> transformed >> stored (ETL)

## Streaming architectures

- When real time analysis is needed

## Architecting for compliance

- GDPR and other similar local regulations
    - Consent from individual
    - Right to have data deleted

- Portability is important for health data

- Financial data might have specific requirements

## Choosing the right technologies

- Location
    - Cloud data systems is the most popular solution due to flexibility and scalability
    - On-premise systems
    - Hybrid: part of the system might be on-premise due to regulations or specific needs

- Monolith vs Modular Systems
    - Monolith
        - Tightly-coupled components, where one 'solution' is served;
        - Good for simplicity, but harder to maintain
    - Modular
        - Loosely-coupled components, self-contained
        - Emerge as 'microservices'
        - Interoperability
        - Great to switch between tools as tech evolves

- Cost Optimisation and business value
     - Total cost of ownership (TCO): Total estimate cost of a solution, project or initiative over its entire lifecycle, including direct and indirect (overhead) costs


    - Total opportunity cost of ownership (TOCO): Cost of lost opportunities that incur in choosing a particular tool or tech. 

     - FinOps: Minimise costs associated with your systems


- Compute options
    - Server: You set up and manage server

    - Container: Modular unit that packages code and dependencies that run on a server

    - Serverless: It's a term used to say you don't need to set-up or maintain the server; typically uses containers. Serverless is good for simple and discrete tasks.

    - You need to determine before event rates, event duration and cost per event to decide which solution makes more sense


## AWS Well-Architected Framework

- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Sustainability