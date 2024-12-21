# SmartCommerce Project Overview

## Project Description

This project focuses on developing the SmartCommerce platform, including the following apps: `core, courses, marketplace, payment`.

## Project Team

- **Project Manager**: [PM](projectmanager.md)
- **Tech Lead**: [Tech Lead](techlead.md)
- **Developers**: 3 people.

For detailed responsibilities, please refer to the roles' specific pages.

## SDLC Overview

```mermaid
gantt
  dateFormat  YYYY-MM-DD
  axisFormat %Y-%m-%d
  title SDLC Overview

  section 1. Analysis (2024-12-21 to 2024-12-28)
    Define project goals and objectives. : 2024-12-21, 2024-12-28
    Collect user requirements and business needs. : 2024-12-21, 2024-12-28
    Identify system stakeholders and their needs. : 2024-12-21, 2024-12-28
    Analyze feasibility and define project scope : 2024-12-21, 2024-12-28
    %% Roles: Product Owner, Project Manager, Business Analyst, CTO %%
  section 2. Plan (2024-12-28 to 2025-01-04)
    Create project timeline and schedule. : 2024-12-28, 2025-01-04
    Estimate required resources (developers, budget, etc) : 2024-12-28, 2025-01-04
    Plan resource allocation : 2024-12-28, 2025-01-04
    Identify risks and mitigation strategies : 2024-12-28, 2025-01-04
    Prepare a development plan : 2024-12-28, 2025-01-04
    %% Roles: Project Manager, CTO %%
  section 3. Design (2025-01-04 to 2025-01-18)
    Design system architecture : 2025-01-04, 2025-01-18
    Create database schema : 2025-01-04, 2025-01-18
    Plan out APIs : 2025-01-04, 2025-01-18
    Design user interface (UI) and user experience (UX) : 2025-01-04, 2025-01-18
    Establish system entry points (web) : 2025-01-04, 2025-01-18
    %% Roles: System Architect, UX/UI designers %%
  section 4. Code (2025-01-18 to 2025-03-15)
    Implement core app logic and functionality : 2025-01-18, 2025-03-15
    Develop front-end interfaces : 2025-01-18, 2025-03-15
    Develop back-end APIs and services : 2025-01-18, 2025-03-15
    Integrate UI/UX designs : 2025-01-18, 2025-03-15
    Write user guide documents : 2025-01-18, 2025-03-15
    Build function libraries : 2025-01-18, 2025-03-15
    %% Roles: Front-end Devs, Back-end Devs %%
  section 5. QC (Quality Control) (2025-03-15 to 2025-03-29)
    Execute unit testing : 2025-03-15, 2025-03-29
    Perform integration testing : 2025-03-15, 2025-03-29
    Carry out system testing : 2025-03-15, 2025-03-29
    Conduct user acceptance testing (UAT) : 2025-03-15, 2025-03-29
    Identify and track all discovered bugs : 2025-03-15, 2025-03-29
    %% Roles: Solutions Architect, QC Engineer, Tester, DevOps, Trial, Users Test %%
  section 6. Deploy (2025-03-29 to 2025-04-05)
    Setup deployment environment : 2025-03-29, 2025-04-05
    Deploy application to server or cloud : 2025-03-29, 2025-04-05
    Configure database : 2025-03-29, 2025-04-05
    Setup user accounts : 2025-03-29, 2025-04-05
    Monitor the system post-deployment : 2025-03-29, 2025-04-05
    %% Roles: DevOps, Database Admin, Business (sign) %%
  section 7. Maintenance (Starting: 2025-04-05)
    Monitor system for issues : 2025-04-05, 1d
    Address and resolve bugs : 2025-04-05, 1d
    Gather user feedback and requests : 2025-04-05, 1d
    Plan future updates and enhancements : 2025-04-05, 1d
    Maintain system documentation : 2025-04-05, 1d
    %% Roles: Users, Testers, Support Managers %%
```

## Detailed Stages

### 1. Analysis

- **Description:** Gather initial requirements and understand project scope.
- **Documentation Directory:** [1. Analysis](./01. 1. Analysis)
- **Tasks:**
  - Define project goals and objectives.
  - Collect user requirements and business needs.
  - Identify system stakeholders and their needs.
  - Analyze feasibility and define project scope

- **Deliverables:**
  - SOW (Statement of Work)
  - Requirements List
  - Collected Data
  - Testing Method Strategy
  - Budget Allocation
  - High-Level Architecture Plan

- **Timeline:**
  - **Start:** 2024-12-21
  - **End:** 2024-12-28

- **Roles:**
  - Product Owner
  - Project Manager
  - Business Analyst
  - CTO


### 2. Plan

- **Description:** Plan the project's schedule, resources, and dependencies.
- **Documentation Directory:** [2. Plan](./02. 2. Plan)
- **Tasks:**
  - Create project timeline and schedule.
  - Estimate required resources (developers, budget, etc)
  - Plan resource allocation
  - Identify risks and mitigation strategies
  - Prepare a development plan

- **Deliverables:**
  - Project Plan
  - Timeline Schedule
  - Resource Allocation List

- **Timeline:**
  - **Start:** 2024-12-28
  - **End:** 2025-01-04

- **Roles:**
  - Project Manager
  - CTO


### 3. Design

- **Description:** Design the software architecture and user interface.
- **Documentation Directory:** [3. Design](./03. 3. Design)
- **Tasks:**
  - Design system architecture
  - Create database schema
  - Plan out APIs
  - Design user interface (UI) and user experience (UX)
  - Establish system entry points (web)

- **Deliverables:**
  - Diagram of software architecture
  - Entry points list (web)
  - API Endpoints list
  - UI/UX Designs

- **Timeline:**
  - **Start:** 2025-01-04
  - **End:** 2025-01-18

- **Roles:**
  - System Architect
  - UX/UI designers


### 4. Code

- **Description:** Write the source code for the software.
- **Documentation Directory:** [4. Code](./04. 4. Code)
- **Tasks:**
  - Implement core app logic and functionality
  - Develop front-end interfaces
  - Develop back-end APIs and services
  - Integrate UI/UX designs
  - Write user guide documents
  - Build function libraries

- **Deliverables:**
  - Source code
  - User guide documentation
  - Function libraries

- **Timeline:**
  - **Start:** 2025-01-18
  - **End:** 2025-03-15

- **Roles:**
  - Front-end Devs
  - Back-end Devs


### 5. QC (Quality Control)

- **Description:** Test the software to identify and fix bugs.
- **Documentation Directory:** [5. QC (Quality Control)](./05. 5. QC (Quality Control))
- **Tasks:**
  - Execute unit testing
  - Perform integration testing
  - Carry out system testing
  - Conduct user acceptance testing (UAT)
  - Identify and track all discovered bugs

- **Deliverables:**
  - List of bugs and issues
  - Testing reports

- **Timeline:**
  - **Start:** 2025-03-15
  - **End:** 2025-03-29

- **Roles:**
  - Solutions Architect
  - QC Engineer
  - Tester
  - DevOps
  - Trial, Users Test


### 6. Deploy

- **Description:** Deploy the software to the production environment.
- **Documentation Directory:** [6. Deploy](./06. 6. Deploy)
- **Tasks:**
  - Setup deployment environment
  - Deploy application to server or cloud
  - Configure database
  - Setup user accounts
  - Monitor the system post-deployment

- **Deliverables:**
  - Ready to run software

- **Timeline:**
  - **Start:** 2025-03-29
  - **End:** 2025-04-05

- **Roles:**
  - DevOps
  - Database Admin
  - Business (sign)


### 7. Maintenance

- **Description:** Provide ongoing support and enhancements.
- **Documentation Directory:** [7. Maintenance](./07. 7. Maintenance)
- **Tasks:**
  - Monitor system for issues
  - Address and resolve bugs
  - Gather user feedback and requests
  - Plan future updates and enhancements
  - Maintain system documentation

- **Deliverables:**
  - Drawbacks and issues
  - Next Version Plan
  - User feedback

- **Timeline:**
  - **Start:** 2025-04-05
  - **End:** Ongoing

- **Roles:**
  - Users
  - Testers
  - Support Managers


