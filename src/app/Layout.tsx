import { Layout as ShellLayout } from '@commonlab/shell'
import { NAV } from './nav'
import { CommandPalette } from './palette/CommandPalette'

/** The shared shell's menu rail, with ValenceLab's command search under the collapse button. */
export function Layout() {
  return <ShellLayout nav={NAV} activeBarClass="before:border-sidebar-foreground" afterToggle={(expanded) => <CommandPalette expanded={expanded} />} />
}
