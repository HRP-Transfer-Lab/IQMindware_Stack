/**
 * IQ Mindware deterministic route-builder reference.
 *
 * This is a dependency-free reference for Codex and the IQMindware.com
 * implementation. It is not yet wired to production analytics, storage or UI.
 */

export type AnswerValue = string | string[] | undefined;

export interface RouteAnswers {
  [questionId: string]: AnswerValue;
}

export interface RouteRule {
  route_id: string;
  priority: number;
  required_answers?: Record<string, string[]>;
  score_weights?: Record<string, Record<string, number>>;
}

export interface RouteBuilderConfig {
  selection_policy: {
    base_score_for_required_match: number;
    max_primary_results: number;
    abstain_when_no_required_match: boolean;
  };
  route_rules: RouteRule[];
}

export interface RouteTemplate {
  route_id: string;
  route_status: string[];
  heading_key: string;
  workflow_explanation_key: string;
  available_protocol_route: string[];
  target_functions_in_development: string[];
  evidence_card_ids: string[];
  workflow_support_ids: string[];
  outcome_ids: string[];
  evidence_boundary_key: string;
  primary_cta: string;
}

export interface RouteCopy {
  headings: Record<string, string>;
  workflow_explanations: Record<string, string>;
  module_labels: Record<string, string>;
  coming_soon_labels: Record<string, string>;
  coming_soon_explanations: Record<string, string>;
  evidence_boundaries: Record<string, string>;
  status_copy: Record<string, string>;
  cta_copy: Record<string, string>;
}

export interface EvidenceCard {
  evidence_card_id: string;
  public_name: string;
  component_ids: string[];
  evidence_profile: Record<
    "scientific_basis" | "exact_implementation" | "training_benefit" | "workflow_transfer",
    { level: string; label: string; summary: string }
  >;
  supported_public_claim: string;
  required_boundary: string;
}

export interface FutureComponent {
  component_id: string;
  status: "coming_soon";
  nearest_available_foundation?: string;
}

function values(value: AnswerValue): string[] {
  if (value === undefined) return [];
  return Array.isArray(value) ? value : [value];
}

function hasRequiredAnswers(
  answers: RouteAnswers,
  required: Record<string, string[]> = {},
): boolean {
  return Object.entries(required).every(([questionId, allowed]) =>
    values(answers[questionId]).some((answer) => allowed.includes(answer)),
  );
}

export function selectRoute(
  answers: RouteAnswers,
  config: RouteBuilderConfig,
): { routeId: string; score: number } | null {
  const candidates = config.route_rules
    .filter((rule) => hasRequiredAnswers(answers, rule.required_answers))
    .map((rule) => {
      let score = config.selection_policy.base_score_for_required_match;

      for (const [questionId, weights] of Object.entries(rule.score_weights ?? {})) {
        for (const answer of values(answers[questionId])) {
          score += weights[answer] ?? 0;
        }
      }

      return { routeId: rule.route_id, score, priority: rule.priority };
    })
    .sort(
      (a, b) =>
        b.score - a.score ||
        b.priority - a.priority ||
        a.routeId.localeCompare(b.routeId),
    );

  if (candidates.length === 0) return null;
  return { routeId: candidates[0].routeId, score: candidates[0].score };
}

export function buildRoutePayload(params: {
  route: RouteTemplate;
  copy: RouteCopy;
  evidenceById: Record<string, EvidenceCard>;
  futureById: Record<string, FutureComponent>;
  supportsById: Record<
    string,
    { workflow_support_id: string; label: string; description: string; locus: string }
  >;
  outcomesById: Record<
    string,
    { outcome_id: string; label: string; level: string; interpretation: string }
  >;
  versions: {
    ontology: string;
    evidence: string;
    availability: string;
    route_config: string;
    copy: string;
  };
}) {
  const {
    route,
    copy,
    evidenceById,
    futureById,
    supportsById,
    outcomesById,
    versions,
  } = params;

  return {
    route_id: route.route_id,
    heading: copy.headings[route.heading_key],
    status_labels: route.route_status.map((status) => copy.status_copy[status]),
    workflow_explanation:
      copy.workflow_explanations[route.workflow_explanation_key],
    available_protocol_route: route.available_protocol_route.map((stepId) => ({
      step_id: stepId,
      label: copy.module_labels[stepId],
      availability: "available_now" as const,
    })),
    coming_soon_targets: route.target_functions_in_development.map((componentId) => ({
      component_id: componentId,
      label: copy.coming_soon_labels[componentId] ?? componentId,
      availability: futureById[componentId]?.status ?? "coming_soon",
      nearest_available_foundation:
        futureById[componentId]?.nearest_available_foundation ?? null,
      explanation: copy.coming_soon_explanations[componentId] ?? null,
    })),
    evidence_cards: route.evidence_card_ids.map((cardId) => evidenceById[cardId]),
    workflow_supports: route.workflow_support_ids.map(
      (supportId) => supportsById[supportId],
    ),
    outcomes: route.outcome_ids.map((outcomeId) => outcomesById[outcomeId]),
    evidence_boundary: copy.evidence_boundaries[route.evidence_boundary_key],
    primary_cta: copy.cta_copy[route.primary_cta],
    versions,
  };
}

/**
 * Implementation rules:
 *
 * 1. Run this entirely in the browser for the first release.
 * 2. Show the route result before requesting contact information.
 * 3. Never put a coming-soon component into available_protocol_route.
 * 4. Do not infer clinical intent from a cognitive score.
 * 5. Fail closed when a required ID, version or checksum is missing.
 * 6. Keep analytics limited to route-builder interaction events; do not send
 *    health context or cognitive preference answers to advertising platforms.
 */
