from crewai import Agent

cross_border_tax_validator = Agent(
    role="Cross Border Tax Validator",
    goal="Deliver high-precision autonomous Cross Border Tax Validator operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
