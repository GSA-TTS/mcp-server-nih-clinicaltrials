def register_prompts(mcp):
    @mcp.prompt(name="clinicaltrials-unavailable-fields")
    def unavailable_fields() -> str:
        return """\
The ClinicalTrials.gov API does not expose the following fields. If a user asks
about any of them, explain that the information is not available through this server:

- Version number: studies do not carry a version identifier in the API
- Protocol amendment history: individual amendment versions are not exposed
- Internal review board (IRB) approval documents: not accessible via the API
- Full investigator contact details beyond name/role: phone and email are
  sometimes present but not guaranteed
- Raw uploaded documents (protocols, SAPs, ICFs): metadata is available via
  LargeDoc fields but the document files themselves are not returned by the API
- Regulatory submission IDs (IND, IDE numbers): not surfaced as structured fields
"""