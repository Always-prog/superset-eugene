import { Metric, styled, t } from '@superset-ui/core';
import { Dropdown, Menu, Space } from 'antd';
import React from 'react';
import { ColumnTypeLabel } from '@superset-ui/chart-controls';

const ExpressionIconContainer = styled('span')`
  ${({ theme }) => `
  div:first-child {
  background-color: ${theme.colors.primary.base}66;
  border-radius: 8px;
}
`}
`;

const StyledMenu = styled(Menu)`
  ${({ theme }) => `
  background-color: ${theme.colors.grayscale.dark2}cc;
  pointer-events: none;
  color: ${theme.colors.grayscale.light4};
`}
`;

const StyledMenuItem = styled(Menu.Item)`
  ${({ theme }) => `
  padding: 5px;
  color: ${theme.colors.grayscale.light4};
  width: 500px;
  overflow: hidden;
  text-wrap: pretty;
`}
`;

export default function MetricsDescription({ metrics }: { metrics: Metric[] }) {
  const menu = (
    <StyledMenu>
      <h3 style={{ textAlign: 'center' }}>{t('Used metrics list')}</h3>
      {metrics.map(metric => (
        <StyledMenuItem>
          {metric.verbose_name} - {metric.description}
        </StyledMenuItem>
      ))}
    </StyledMenu>
  );
  return (
    <Dropdown overlay={menu}>
      <Space>
        <ExpressionIconContainer>
          <ColumnTypeLabel type="expression" />
        </ExpressionIconContainer>
      </Space>
    </Dropdown>
  );
}
