import datetime
import json
import os


def generate_project_markdown(project_name, apps, team, template, output_dir="."):
    """Generates a project markdown file with separate sections for each role and stage directories."""

    roles = ["Project Manager", "Tech Lead", "Engineers"]

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create stage-specific directories
    for i, (stage_name, _) in enumerate(template["SDLC Stages"].items()):
        stage_dir = os.path.join(
            output_dir, f"{stage_name}"
        )  # Format: "01. Analysis"{i+1:02d}. 
        os.makedirs(
            stage_dir, exist_ok=True
        )  # exist_ok = True does not throw error if the dir is already exists

    # Create a main project README.md
    main_file_path = os.path.join(output_dir, "README.md")
    with open(main_file_path, "w") as main_file:
        main_file.write(f"# {project_name} Project Overview\n\n")
        main_file.write(f"## Project Description\n\n")
        main_file.write(
            f"This project focuses on developing the {project_name} platform, including the following apps: `{', '.join(apps)}`.\n\n"
        )

        main_file.write("## Project Team\n\n")
        main_file.write(
            f"- **Project Manager**: [{team['Project Manager']}](projectmanager.md)\n"
        )
        main_file.write(f"- **Tech Lead**: [{team['Tech Lead']}](techlead.md)\n")
        main_file.write(f"- **Developers**: {team['Developers']} people.\n\n")
        main_file.write(
            "For detailed responsibilities, please refer to the roles' specific pages.\n\n"
        )

        main_file.write(f"## SDLC Overview\n\n")
        main_file.write(mermaid_sdlc_diagram(template))
        main_file.write("\n\n")
        main_file.write("## Detailed Stages\n\n")

        for i, (stage_name, stage_details) in enumerate(
            template["SDLC Stages"].items()
        ):
            main_file.write(f"### {stage_name}\n\n")
            main_file.write(f"- **Description:** {stage_details['Description']}\n")
            main_file.write(
                f"- **Documentation Directory:** [{stage_name}](./{i+1:02d}. {stage_name})\n"
            )

            main_file.write("- **Tasks:**\n")
            for task in stage_details["Tasks"]:
                main_file.write(f"  - {task}\n")
            main_file.write("\n")

            main_file.write("- **Deliverables:**\n")
            for deliverable in stage_details["Deliverables"]:
                main_file.write(f"  - {deliverable}\n")
            main_file.write("\n")

            main_file.write("- **Timeline:**\n")
            main_file.write(f"  - **Start:** {stage_details['Timeline']['Start']}\n")
            main_file.write(f"  - **End:** {stage_details['Timeline']['End']}\n")
            main_file.write("\n")

            main_file.write("- **Roles:**\n")
            for role in stage_details["Roles"]:
                main_file.write(f"  - {role}\n")
            main_file.write("\n")

            main_file.write("\n")

    # Generate separate files for roles
    for role in roles:
        role_file_path = os.path.join(output_dir, f"{role.lower().replace(' ', '')}.md")
        if role == "Project Manager":
            role_file_path = os.path.join(output_dir, "projectmanager.md")
        with open(role_file_path, "w") as role_file:
            role_file.write(f"# {role} Responsibilities\n\n")
            role_file.write("## Project Tasks:\n\n")
            for stage_name, stage_details in template["SDLC Stages"].items():
                if role in stage_details["Roles"]:
                    role_file.write(f"### {stage_name} Tasks:\n")
                    for task in stage_details["Tasks"]:
                        role_file.write(f"  - {task}\n")
                    role_file.write("\n")

            role_file.write("## Relevant Deliverables\n\n")
            for stage_name, stage_details in template["SDLC Stages"].items():
                if role in stage_details["Roles"]:
                    role_file.write(f"### {stage_name} Deliverables:\n")
                    for deliverable in stage_details["Deliverables"]:
                        role_file.write(f"- {deliverable}\n")
                    role_file.write("\n")


def mermaid_sdlc_diagram(template):
    """Generates a Mermaid diagram for the SDLC process."""
    mermaid_code = "```mermaid\n"
    mermaid_code += "graph LR\n"

    for i, (stage_name, _) in enumerate(template["SDLC Stages"].items()):
        mermaid_code += f"  {i+1}({stage_name}) --> "
        if i < len(template["SDLC Stages"]) - 1:
            mermaid_code += f"{i+2}\n"
        else:
            mermaid_code += "End\n"

    mermaid_code += "```"
    return mermaid_code


def generate_project_template(project_name, apps, team_size, pm_name, tech_lead_name):
    """Generates a software development template based on SDLC."""

    template = {
        "Project": project_name,
        "Apps": apps,
        "Team": {
            "Size": team_size,
            "Project Manager": pm_name,
            "Tech Lead": tech_lead_name,
            "Developers": team_size - 2,  # Subtract PM and Tech Lead
        },
        "SDLC Stages": {
            "1. Analysis": {
                "Description": "Gather initial requirements and understand project scope.",
                "Tasks": [
                    "Define project goals and objectives.",
                    "Collect user requirements and business needs.",
                    "Identify system stakeholders and their needs.",
                    "Analyze feasibility and define project scope",
                ],
                "Deliverables": [
                    "SOW (Statement of Work)",
                    "Requirements List",
                    "Collected Data",
                    "Testing Method Strategy",
                    "Budget Allocation",
                    "High-Level Architecture Plan",
                ],
                "Timeline": {
                    "Start": datetime.date.today(),
                    "End": datetime.date.today()
                    + datetime.timedelta(days=7),  # Example: 1 week
                },
                "Roles": [
                    "Product Owner",
                    "Project Manager",
                    "Business Analyst",
                    "CTO",
                ],
            },
            "2. Plan": {
                "Description": "Plan the project's schedule, resources, and dependencies.",
                "Tasks": [
                    "Create project timeline and schedule.",
                    "Estimate required resources (developers, budget, etc)",
                    "Plan resource allocation",
                    "Identify risks and mitigation strategies",
                    "Prepare a development plan",
                ],
                "Deliverables": [
                    "Project Plan",
                    "Timeline Schedule",
                    "Resource Allocation List",
                ],
                "Timeline": {
                    "Start": datetime.date.today()
                    + datetime.timedelta(
                        days=7
                    ),  # Example: Starts 1 week after Analysis
                    "End": datetime.date.today()
                    + datetime.timedelta(days=14),  # Example: 1 week for Planning
                },
                "Roles": ["Project Manager", "CTO"],
            },
            "3. Design": {
                "Description": "Design the software architecture and user interface.",
                "Tasks": [
                    "Design system architecture",
                    "Create database schema",
                    "Plan out APIs",
                    "Design user interface (UI) and user experience (UX)",
                    "Establish system entry points (web)",
                ],
                "Deliverables": [
                    "Diagram of software architecture",
                    "Entry points list (web)",
                    "API Endpoints list",
                    "UI/UX Designs",
                ],
                "Timeline": {
                    "Start": datetime.date.today()
                    + datetime.timedelta(days=14),  # Example: Starts 1 week after Plan
                    "End": datetime.date.today()
                    + datetime.timedelta(days=28),  # Example: 2 week for Design
                },
                "Roles": ["System Architect", "UX/UI designers"],
            },
            "4. Code": {
                "Description": "Write the source code for the software.",
                "Tasks": [
                    "Implement core app logic and functionality",
                    "Develop front-end interfaces",
                    "Develop back-end APIs and services",
                    "Integrate UI/UX designs",
                    "Write user guide documents",
                    "Build function libraries",
                ],
                "Deliverables": [
                    "Source code",
                    "User guide documentation",
                    "Function libraries",
                ],
                "Timeline": {
                    "Start": datetime.date.today()
                    + datetime.timedelta(
                        days=28
                    ),  # Example: Starts 2 week after Design
                    "End": datetime.date.today()
                    + datetime.timedelta(days=84),  # Example: 8 week for Coding
                },
                "Roles": ["Front-end Devs", "Back-end Devs"],
            },
            "5. QC (Quality Control)": {
                "Description": "Test the software to identify and fix bugs.",
                "Tasks": [
                    "Execute unit testing",
                    "Perform integration testing",
                    "Carry out system testing",
                    "Conduct user acceptance testing (UAT)",
                    "Identify and track all discovered bugs",
                ],
                "Deliverables": ["List of bugs and issues", "Testing reports"],
                "Timeline": {
                    "Start": datetime.date.today()
                    + datetime.timedelta(days=84),  # Example: Starts 8 week after Code
                    "End": datetime.date.today()
                    + datetime.timedelta(days=98),  # Example: 2 week for Testing
                },
                "Roles": [
                    "Solutions Architect",
                    "QC Engineer",
                    "Tester",
                    "DevOps",
                    "Trial, Users Test",
                ],
            },
            "6. Deploy": {
                "Description": "Deploy the software to the production environment.",
                "Tasks": [
                    "Setup deployment environment",
                    "Deploy application to server or cloud",
                    "Configure database",
                    "Setup user accounts",
                    "Monitor the system post-deployment",
                ],
                "Deliverables": ["Ready to run software"],
                "Timeline": {
                    "Start": datetime.date.today()
                    + datetime.timedelta(days=98),  # Example: Starts 2 week after QC
                    "End": datetime.date.today()
                    + datetime.timedelta(days=105),  # Example: 1 week for Deployment
                },
                "Roles": ["DevOps", "Database Admin", "Business (sign)"],
            },
            "7. Maintenance": {
                "Description": "Provide ongoing support and enhancements.",
                "Tasks": [
                    "Monitor system for issues",
                    "Address and resolve bugs",
                    "Gather user feedback and requests",
                    "Plan future updates and enhancements",
                    "Maintain system documentation",
                ],
                "Deliverables": [
                    "Drawbacks and issues",
                    "Next Version Plan",
                    "User feedback",
                ],
                "Timeline": {
                    "Start": datetime.date.today()
                    + datetime.timedelta(
                        days=105
                    ),  # Example: Starts 1 week after Deployment
                    "End": "Ongoing",
                },
                "Roles": ["Users", "Testers", "Support Managers"],
            },
        },
    }
    return template


# Project details
project_name = "SmartCommerce"
apps = ["core", "courses", "marketplace", "payment"]
team_size = 5  # 5 dev + 1 PM
pm_name = "PM"
tech_lead_name = "Tech Lead"
output_directory = "SDLC"  # Output directory to save all generated files


# Generate the template
template = generate_project_template(
    project_name, apps, team_size, pm_name, tech_lead_name
)
generate_project_markdown(
    project_name, apps, template["Team"], template, output_dir=output_directory
)
print(f"Project documentation has been generated in the '{output_directory}' folder")
