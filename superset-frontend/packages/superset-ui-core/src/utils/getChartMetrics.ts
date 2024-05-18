import { QueryFormData } from '../query';

export default function getChartMetrics(formData: QueryFormData) {
  const metrics = [];
  if (formData.metrics && Array.isArray(formData.metrics)) {
    metrics.push(...formData.metrics);
  }
  if (formData.metric) {
    metrics.push(formData.metric);
  }
  return metrics;
}
