# Compact production record

Keep one brief/ledger rather than creating a file per tiny revision. Omit irrelevant fields. For multiple generation attempts, retain a list of the generation records below; never overwrite an earlier job or its unknown charge state. Track confirmed, reserved and unknown spend separately. An unresolved job remains unresolved after checking it and does not authorize resubmission.

```yaml
project:
  intent: ""
  mode: explore
  current_project: ""
  approved_comp: ""
  approved_render: ""
  duration_seconds: null
  fps: null
  aspect_ratio: ""
  audio_source: ""
  audio_excerpt_start: null
  audio_excerpt_end: null
identity:
  reference: ""
  fixed_features: []
scene:
  fixed_properties: []
  palette_roles: {}
  reference_links: []
shots:
  - id: hero
    timeline_interval: []
    start_frame: ""
    body_action: ""
    camera_action: ""
    effects_action: ""
    musical_accents: []
    end_handoff: ""
    acceptance_criteria: []
generation:
  provider: ""
  exact_model: ""
  duration_seconds: null
  resolution: ""
  audio_setting: silent
  allowed_takes: null
  total_authorized_cap: null
  unit: ""
  live_quote: null
  job_id: ""
  charge_confirmed: null
  status: not_submitted
review:
  defect: ""
  changed_interval: []
  result: ""
  unresolved: []
delivery:
  files: []
  technical_checks: []
  visual_checks: []
  audio_checks: []
  project_relocation_checked: false
  published: false
```

Numbers, filenames and statuses are placeholders, not authorization or measured results.
