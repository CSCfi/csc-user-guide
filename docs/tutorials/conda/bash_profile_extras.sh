#!/bin/bash

# Helper functions

# Prepends the given path to PATH environment variable and removes duplicates
prependpath () {
    PATH="$1:${PATH}:"
    PATH="${PATH//:$1}"
    PATH="${PATH%:}"
}

boxprint () {
    local s=$(cat)
    local w=$(wc -L <<<"$s")
    printf "$FONT_BOLD$COLOR_GREEN"
    printf '*%.0s' $(seq 1 $((w + 6))); printf "\n"
    while read l; do
        printf "*  %-${w}s  *\n" "$l"
    done <<<"$s"
    printf '*%.0s' $(seq 1 $((w + 6))); printf "\n"
    printf "$FONT_RESET"
}

tsetgid () {
    [[ $(stat -c "%a"  $1) =~ ^[26] ]]
}

tdefaultfacl () {
    getfacl $1 | grep -q ^default
}

condaroot=$WRKDIR/DONOTREMOVE/conda

# Add conda shell functions
source ${condaroot}/miniconda3/etc/profile.d/conda.sh

# Screaming prompt
FONT_RESET=$(tput sgr0)
FONT_BOLD=$(tput bold)
COLOR_RED=$(tput setaf 1)
COLOR_GREEN=$(tput setaf 2)
PS1="\[${FONT_RESET}${COLOR_RED}\]\u@${HOSTNAME%-*} \w \$ \[${FONT_BOLD}\]"
trap 'echo -ne "${FONT_RESET}" > $(tty)' DEBUG

# Alias
alias xt="printf '\e[2t'; gnome-terminal &"
alias ls="ls --color"
$(
    emacs=/wrk/jle/DONOTREMOVE/conda/miniconda3/envs/conda-forge/bin/emacs
    [ -x $emacs ] && echo "alias emacs=$emacs"
)

# Unload all modules to clean up LD_LIBRARY_PATH
module purge

# Set primary group and umask for software installs
umask 0002

# Notification
boxprint <<EOF

Environment for Conda admin work for user '$(whoami)':
\    Module list:  $(module list 2>&1 | head -1)
\    UMASK:        $(umask)
\    PATH:         $(printf '%s\n\\                  ' ${PATH//:/ } | head -n -1)
\    Group:        $(id -gn)

Setgid bit $(tsetgid $condaroot && echo is || echo is not) set for \
conda root
\    $(ls -dlh --color=never $condaroot | awk '{print $1,$3,$4,$NF}' | head -1)

Conda root file access control list info:
$(getfacl $condaroot | sed '$ ! s/^/\\    /')

Run 'conda info' to check conda defaults

EOF
