// DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
package types

import (
	"gopkg.in/validator.v2"
)

type Aci struct {
	Groups int32  `json:"groups,omitempty"`
	Hash   string `json:"hash" validate:"nonzero"`
	Right  string `json:"right" validate:"nonzero"`
	Uid    int32  `json:"uid" validate:"nonzero"`
	Users  int32  `json:"users,omitempty"`
}

func (s Aci) Validate() error {

	return validator.Validate(s)
}
