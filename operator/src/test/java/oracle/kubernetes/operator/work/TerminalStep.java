// Copyright 2019, Oracle Corporation and/or its affiliates.  All rights reserved.
// Licensed under the Universal Permissive License v 1.0 as shown at
// http://oss.oracle.com/licenses/upl.

package oracle.kubernetes.operator.work;

/** A do-nothing step that can be used as a base for testing. It has no next step. */
public class TerminalStep extends Step {
  private boolean executed;

  public TerminalStep() {
    super(null);
  }

  public boolean wasRun() {
    return executed;
  }

  @Override
  public NextAction apply(Packet packet) {
    executed = true;
    return doNext(packet);
  }
}
