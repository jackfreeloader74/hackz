# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attkprogmap(models.Model):
    attackid = models.IntegerField(db_column='AttackID', blank=True, null=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttkProgMap'


class Attkrefmap(models.Model):
    attackid = models.TextField(db_column='AttackID', blank=True, null=True)  # Field name made lowercase.
    reference = models.TextField(db_column='Reference', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttkRefMap'


class Attks(models.Model):
    attackid = models.AutoField(db_column='AttackID')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    target = models.TextField(db_column='Target', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attks'


class Cmdrefmap(models.Model):
    cmdid = models.IntegerField(db_column='CmdID', blank=True, null=True)  # Field name made lowercase.
    ref = models.TextField(db_column='Ref', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CmdRefMap'


class Cmdtagmap(models.Model):
    cmdid = models.IntegerField(db_column='CmdID', blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CmdTagMap'


class Cmds(models.Model):
    commandid = models.AutoField(db_column='CommandID', blank=True, null=True)  # Field name made lowercase.
    command = models.TextField(db_column='Command')  # Field name made lowercase. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    program = models.TextField(db_column='Program', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cmds'


class Progrefmap(models.Model):
    programid = models.IntegerField(db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.
    reference = models.TextField(db_column='Reference', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProgRefMap'


class Progstgmap(models.Model):
    programid = models.IntegerField(db_column='ProgramID', blank=True, null=True)  # Field name made lowercase.
    stage = models.TextField(db_column='Stage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProgStgMap'


class Progs(models.Model):
    programid = models.AutoField(db_column='ProgramID')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    target = models.TextField(db_column='Target', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Progs'
